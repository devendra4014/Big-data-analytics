package com.sunbeam;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class EmpReducer extends Reducer<Text, DoubleWritable, Text, DoubleWritable> {
	private DoubleWritable avgSalWr = new DoubleWritable();
	@Override
	protected void reduce(Text key, Iterable<DoubleWritable> values,
			Reducer<Text, DoubleWritable, Text, DoubleWritable>.Context context) throws IOException, InterruptedException {
		double total = 0.0;
		int count = 0;
		for(DoubleWritable salWr:values) {
			double sal = salWr.get();
			total = total + sal;
			count++;
		}
		double avgSal = total / count;
		avgSalWr.set(avgSal);
		context.write(key, avgSalWr);
	}
}
