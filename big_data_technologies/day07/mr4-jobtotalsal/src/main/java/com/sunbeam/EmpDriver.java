package com.sunbeam;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.mapreduce.lib.partition.HashPartitioner;
import org.apache.hadoop.util.GenericOptionsParser;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class EmpDriver extends Configured implements Tool {
	public static void main(String[] args) {
		try {
			GenericOptionsParser parser = new GenericOptionsParser(args);
			Configuration conf = parser.getConfiguration();
			
			EmpDriver driver = new EmpDriver();
			int ret = ToolRunner.run(conf, driver, args);
			System.exit(ret);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	@Override
	public int run(String[] args) throws Exception {
		// validate command line args
		if(args.length != 2) {
			System.out.println("Invalid command line arguments.");
			System.out.println("Syntax: hadoop jar app.jar /path/of/input /path/of/output");
			System.exit(1);
		}
		// create a new MR job and assign name
		Configuration conf = this.getConf();
		Job job = Job.getInstance(conf, "JobwiseTotalSal");
		// mention jar in which mapper and reducer class is available
		job.setJarByClass(EmpDriver.class);
		// give mapper class and its output key/value type
		job.setMapperClass(EmpMapper.class);
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(DoubleWritable.class);
		// give reducer class and its output key/value type
		job.setReducerClass(EmpReducer.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(DoubleWritable.class);
		// set combiner class
		job.setCombinerClass(EmpReducer.class);
		// set number of reducers
		job.setNumReduceTasks(2);
		// set the partitioner class
		//job.setPartitionerClass(HashPartitioner.class); // default partitioner class
		job.setPartitionerClass(EmpPartitioner.class); // custom partitioner
		// give input format and output format
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		// give input & output dir path (of hdfs)
		TextInputFormat.setInputPaths(job, args[0]);
		TextOutputFormat.setOutputPath(job, new Path(args[1]));
		// submit job to cluster and wait for its completion
		job.submit();
		boolean success = job.waitForCompletion(true);
		int ret = success ? 0 : 1;
		return ret;
	}
}
