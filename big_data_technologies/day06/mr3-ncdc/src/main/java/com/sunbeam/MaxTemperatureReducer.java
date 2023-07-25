package com.sunbeam;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MaxTemperatureReducer extends Reducer<NullWritable, Text, IntWritable, DoubleWritable> {
	private IntWritable maxMonthWr = new IntWritable();
	private DoubleWritable maxTemperatureWr = new DoubleWritable();
	@Override
	protected void reduce(NullWritable key, Iterable<Text> values,
			Reducer<NullWritable, Text, IntWritable, DoubleWritable>.Context context)
			throws IOException, InterruptedException {
        double maxTemperature = -Double.MIN_VALUE;
        int maxMonth = 0;
        for(Text monthTemperatureWr: values) {
            String monthTemperature = monthTemperatureWr.toString();
            String[] parts = monthTemperature.split(",");
            int month = Integer.parseInt(parts[0]);
            double temperature = Double.parseDouble(parts[1]);
            if(temperature > maxTemperature) {
                maxTemperature = temperature;
                maxMonth = month;
            }
        }
        maxMonthWr.set(maxMonth);
        maxTemperatureWr.set(maxTemperature);
        context.write(maxMonthWr, maxTemperatureWr);
	}
}
