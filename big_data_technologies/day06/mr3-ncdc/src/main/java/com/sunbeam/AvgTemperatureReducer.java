package com.sunbeam;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Reducer;

public class AvgTemperatureReducer extends Reducer<IntWritable, DoubleWritable, IntWritable, DoubleWritable> {
	private DoubleWritable avgTemperatureWr = new DoubleWritable();
	@Override
	protected void reduce(IntWritable key, Iterable<DoubleWritable> values,
			Reducer<IntWritable, DoubleWritable, IntWritable, DoubleWritable>.Context context)
			throws IOException, InterruptedException {
		double total = 0.0;
		int count = 0;
		for (DoubleWritable temperatureWr : values) {
			double temperature = temperatureWr.get();
			total = total + temperature;
			count++;
		}
		double avgTemperature = total / count;
		avgTemperatureWr.set(avgTemperature);
		context.write(key, avgTemperatureWr);
	}
}
