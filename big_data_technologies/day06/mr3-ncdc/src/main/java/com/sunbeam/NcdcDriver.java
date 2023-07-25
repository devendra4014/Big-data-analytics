package com.sunbeam;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.CombineTextInputFormat;
import org.apache.hadoop.mapreduce.lib.input.KeyValueTextInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class NcdcDriver extends Configured implements Tool {
	public static void main(String[] args) {
		try {
			GenericOptionsParser parser = new GenericOptionsParser(args);
			Configuration conf = parser.getConfiguration();
			
			NcdcDriver driver = new NcdcDriver();
			int ret = ToolRunner.run(conf, driver, args);
			System.exit(ret);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	@Override
	public int run(String[] args) throws Exception {
		// check command line args -- arg0: input dir, arg1: month avg temp output, arg2: max month & temp
		if(args.length != 3) {
			System.out.println("Insufficient arguments.");
			System.out.println("arg0: input dir, arg1: month avg temp output, arg2: max month & temp");
			return 1;
		}
		// create a new MR job and assign name
		Configuration conf = this.getConf();
		Job job = Job.getInstance(conf, "MonthlyAvgTemperature");
		// mention jar in which mapper and reducer class is available
		job.setJarByClass(NcdcDriver.class);
		// give mapper class and its output key/value type
		job.setMapperClass(AvgTemperatureMapper.class);
		job.setMapOutputKeyClass(IntWritable.class);
		job.setMapOutputValueClass(DoubleWritable.class);
		// give reducer class and its output key/value type
		job.setReducerClass(AvgTemperatureReducer.class);
		job.setOutputKeyClass(IntWritable.class);
		job.setOutputValueClass(DoubleWritable.class);
		// give input format and output format
		//job.setInputFormatClass(TextInputFormat.class);
		job.setInputFormatClass(CombineTextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		// give input & output dir path (of hdfs)
		TextInputFormat.setInputPaths(job, args[0]);
		TextOutputFormat.setOutputPath(job, new Path(args[1]));
		// submit job to cluster and wait for its completion
		job.submit();
		boolean success = job.waitForCompletion(true);
		if(!success)
			return 1;
		// create a new MR job and assign name
		Job job2 = Job.getInstance(conf, "MaxTemperatureMonth");
		// mention jar in which mapper and reducer class is available
		job2.setJarByClass(NcdcDriver.class);
		// give mapper class and its output key/value type
		job2.setMapperClass(MaxTemperatureMapper.class);
		job2.setMapOutputKeyClass(NullWritable.class);
		job2.setMapOutputValueClass(Text.class);
		// give reducer class and its output key/value type
		job2.setReducerClass(MaxTemperatureReducer.class);
		job2.setOutputKeyClass(IntWritable.class);
		job2.setOutputValueClass(DoubleWritable.class);
		// give input format and output format
		job2.setInputFormatClass(KeyValueTextInputFormat.class);
		job2.setOutputFormatClass(TextOutputFormat.class);
		// give input & output dir path (of hdfs)
		TextInputFormat.setInputPaths(job2, args[1]);
		TextOutputFormat.setOutputPath(job2, new Path(args[2]));
		// submit job to cluster and wait for its completion
		job2.submit();
		success = job2.waitForCompletion(true);
		int ret = success ? 0 : 1;
		return ret;
	}
}