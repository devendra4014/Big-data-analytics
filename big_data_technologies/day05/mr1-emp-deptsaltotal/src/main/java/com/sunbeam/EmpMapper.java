package com.sunbeam;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class EmpMapper extends Mapper<LongWritable, Text, IntWritable, DoubleWritable> {
	// create writable objects as fields
	private IntWritable deptWr = new IntWritable();
	private DoubleWritable salWr = new DoubleWritable();
	@Override
	protected void map(LongWritable key, Text value,
			Mapper<LongWritable, Text, IntWritable, DoubleWritable>.Context context)
			throws IOException, InterruptedException {
		String line = value.toString();
		String[] parts = line.split(",");
		int deptno = Integer.parseInt(parts[7]);
		double sal = Double.parseDouble(parts[5]);
		// set values in writable objects and then send to hadoop (via context).
		deptWr.set(deptno);
		salWr.set(sal);
		context.write(deptWr, salWr);
	}
}
