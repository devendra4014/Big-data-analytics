package com.sunbeam;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class EmpMapper extends Mapper<LongWritable, Text, Text, DoubleWritable> {
	private Text jobWr = new Text();
	private DoubleWritable salWr = new DoubleWritable();
	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, DoubleWritable>.Context context)
			throws IOException, InterruptedException {
		String line = value.toString();
		String[] parts = line.split(",");
		String job = parts[2];
		double sal = Double.parseDouble(parts[5]);
		jobWr.set(job);
		salWr.set(sal);
		context.write(jobWr, salWr);
	}
}
