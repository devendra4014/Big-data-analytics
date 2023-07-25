package com.sunbeam;

import java.io.IOException;
import java.util.Arrays;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class AvgTemperatureMapper extends Mapper<LongWritable, Text, IntWritable, DoubleWritable> {
	public static final int INVALID_TEMPERATURE = 9999;
	public static final int[] VALID_QUALITIES = {0, 1, 2, 4, 5, 9};
	private IntWritable monthWr = new IntWritable();
	private DoubleWritable temperatureWr = new DoubleWritable();
	@Override
	protected void map(LongWritable key, Text value,
			Mapper<LongWritable, Text, IntWritable, DoubleWritable>.Context context)
			throws IOException, InterruptedException {
		String line = value.toString();
		try {
			int month = Integer.parseInt(line.substring(19,21));
			double temperature = Double.parseDouble(line.substring(87, 92));
			int quality = Integer.parseInt(line.substring(92,93));
			if(Arrays.binarySearch(VALID_QUALITIES, 0, VALID_QUALITIES.length, quality) != -1 
					&& (int)temperature != INVALID_TEMPERATURE) {
				context.getCounter(NcdcJobCounters.VALID_READING).increment(1);
				monthWr.set(month);
				temperatureWr.set(temperature);
				context.write(monthWr, temperatureWr);
			}
			else {
				context.getCounter(NcdcJobCounters.INVALID_READING).increment(1);
				System.out.println("Invalid Reading: " + line);
			}
		} catch(Exception e) {
			context.getCounter(NcdcJobCounters.INVALID_RECORD).increment(1);
			System.out.println("Invalid Record: " + line);
		}
	}
}
