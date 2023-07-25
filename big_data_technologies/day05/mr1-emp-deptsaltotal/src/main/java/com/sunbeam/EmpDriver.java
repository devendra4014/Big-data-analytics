package com.sunbeam;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class EmpDriver {
	public static void main(String[] args) throws Exception {
		// create a new MR job and assign name
		Configuration conf = new Configuration();
		Job job = Job.getInstance(conf, "DeptwiseTotalSal");
		// mention jar in which mapper and reducer class is available
		job.setJarByClass(EmpDriver.class);
		// give mapper class and its output key/value type
		job.setMapperClass(EmpMapper.class);
		job.setMapOutputKeyClass(IntWritable.class);
		job.setMapOutputValueClass(DoubleWritable.class);
		// give reducer class and its output key/value type
		job.setReducerClass(EmpReducer.class);
		job.setOutputKeyClass(IntWritable.class);
		job.setOutputValueClass(DoubleWritable.class);
		// give input format and output format
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		// give input & output dir path (of hdfs)
		TextInputFormat.setInputPaths(job, "/user/nilesh/emp/input");
		TextOutputFormat.setOutputPath(job, new Path("/user/nilesh/emp/output1"));
		// submit job to cluster and wait for its completion
		job.submit();
		boolean success = job.waitForCompletion(true);
		int ret = success ? 0 : 1;
		System.exit(ret);
	}
}


