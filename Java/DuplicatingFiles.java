package A2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;


public class DuplicatingFiles {
	
	public static void main(String[] args) throws IOException {
				
		//use buffered reader to get input from system.in
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

		//get number of files we are comparing
		int n = Integer.parseInt(input.readLine());

		//compare files as long as number of files is not 0
		while (n != 0) {

			//Create a hashmap which maps file(String) to an integer
			HashMap<String, Integer> hashes = new HashMap<>();

			//loop through all the files in a case
			for (int i = 0; i < n; i++) {
				//get the file from the input
				String file = input.readLine();

				//if the file is not in the hash map, insert the file into the map at value 1
				//if it is a duplicate, increment the value of the file by 1 
				if (!hashes.containsKey(file))
					hashes.put(file, 1);
				else
					hashes.put(file, hashes.get(file) + 1);
			}

			//counter number of times file is repeated
			int repeat = 0;

			//get a file from the hashmap
			for (String file1 : hashes.keySet()) {
				//get hash value using XOR hash function for this file
				char hashFile1 = hashFunction(file1);

				//compare this hash value with all other files in hashmap
				for (String file2 : hashes.keySet()) {
					if (!file1.equals(file2)) {
						char hashFile2 = hashFunction(file2);

						//if the hash values are identical, increment repetitions by getting all the files that are identical 
						if (hashFile1 == hashFile2) {
							int totalRepetitions = hashes.get(file1) * hashes.get(file2);
							repeat = repeat + totalRepetitions;
						}
					}
				}
			}

			System.out.println(hashes.size() + " " + repeat / 2);
			n = Integer.parseInt(input.readLine());

		}

		input.close();
	}
	
	//the exclusive or (XOR) of the ASCII value hash function
	public static char hashFunction(String fileAsString) {
		//use char to represent a byte
		char hashValue = 1;

		for (int i = 0; i < fileAsString.length(); i++)
			//perform XOR with respect to every char in the string and store the result as a char
			hashValue = (char) (hashValue ^ fileAsString.charAt(i));

		return hashValue;
	}
}