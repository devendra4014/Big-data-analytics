package com.sunbeam;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MaxTemperatureMapper extends Mapper<Text, Text, NullWritable, Text> {
	private NullWritable nullWr = NullWritable.get();
	private Text monthTemperatureWr = new Text();
	@Override
	protected void map(Text key, Text value, Mapper<Text, Text, NullWritable, Text>.Context context)
			throws IOException, InterruptedException {
		int month = Integer.parseInt(key.toString());
	    double temperature = Double.parseDouble(value.toString());
	    String monthTemperature = month + "," + temperature;
	    monthTemperatureWr.set(monthTemperature);
	    context.write(nullWr, monthTemperatureWr);
	}
}
