package A1;

import java.util.Scanner;

public class ColdputerScience
{
	public static void main (String[] args) 
	{
		//Scanner class used to get user input
		Scanner scanner = new Scanner(System.in);
		//use nextInt to find out how many temps we have
		int numberOfTemps = scanner.nextInt();
		//keep track of the temps below -
		int numberOfTempsLessThanZero = 0;
		int temp;
		
		//iterate through all the temps
		for (int i = 0 ; i<numberOfTemps; i++)
		{
			temp = scanner.nextInt();
			//increment variable if temp is below 0
			if (temp < 0 ) 
			{
				numberOfTempsLessThanZero++;
			}
		}
		scanner.close();
		System.out.println(numberOfTempsLessThanZero);
	}
			
		
} 
