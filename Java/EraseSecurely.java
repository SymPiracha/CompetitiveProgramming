package A1;

import java.util.Scanner;

public class EraseSecurely
{
	public static void main (String[] args) 
	{
		//Scanner class used to get user input
		Scanner scanner = new Scanner(System.in);
		
		int n = scanner.nextInt();
		
		String lineBeforeDeletion = scanner.next();
		String lineAfterDeletion = scanner.next();
		
		//use boolean b to keep track of process
		boolean b = true;
		
		//iterate through all the chars of a line
		for (int i = 0 ; i<lineBeforeDeletion.length() ; i++) 
		{
			//if n is divisible by 2, that means that line before deletion should be equal to the one after deletion
			if ( n % 2 == 0 ) 
			{
				if ( lineBeforeDeletion.charAt(i) != lineAfterDeletion.charAt(i) )
				{
					b = false;
				}
			}
			else 
			{
				//if n is not divisible by 2, that means that line before deletion should not be equal to the one after deletion
				if (lineBeforeDeletion.charAt(i) == lineAfterDeletion.charAt(i))
				{
					b = false;
				}
			}
		}
		
		if (b)
		{
			System.out.println("Deletion succeeded");
		}
		else
		{
			System.out.println("Deletion failed");
		}
		scanner.close();
	}
}
