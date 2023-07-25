package com.sunbeam;

import java.io.File;
import java.util.Scanner;

public class Demo02Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter a path: ");
		String path = sc.nextLine();
		File file = new File(path);
		if(!file.exists()) {
			System.out.println("Invalid path.");
			System.exit(0);
		}
		if(file.isFile()) {
			System.out.println("File Name: " + file.getName());
			System.out.println("Directory: " + file.getParent());
			System.out.println("File Size: " + file.length() + " bytes");
			System.out.println("Is Hidden: " + file.isHidden());
			String perm = "";
			perm += (file.canRead()?"r":"-");
			perm += (file.canWrite()?"w":"-");
			perm += (file.canExecute()?"x":"-");
			System.out.println("Permissions: " + perm);
		}
		else if(file.isDirectory()) {
			System.out.println("Directory Name: " + file.getName());
			File[] files = file.listFiles();
			for(File f : files)
				System.out.println(" - " + f.getName());
		}
		else
			System.out.println("Neither file nor directory");
		sc.close();
	}
}
