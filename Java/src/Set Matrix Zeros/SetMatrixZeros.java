import java.util.Random;

public class SetMatrixZeros {
	public void setZeros(int[][] matrix) {
		boolean firstRowZero = false;
		boolean firstColumnZero = false;

		for (int i=0; i<matrix.length; i++) {
			if (matrix[i][0] == 0) {
				firstColumnZero = true;
				break;
			}
		}

		for (int i=0; i<matrix[0].length; i++) {
			if (matrix[0][i] == 0) {
				firstRowZero = true;
				break;
			}
		}

		// mark the position to the first row and first column
		for (int i=1; i<matrix.length; i++) {
			for (int j=1; j<matrix[0].length; j++) {
				if (matrix[i][j] == 0) {
					matrix[i][0] = 0;
					matrix[0][j] = 0;
				}
			}
		}

		// this is intended to mark all the inner rows and cols to be 0 except for the 1st row and 1st col. 
		for (int i=1; i<matrix.length; i++) {
			for (int j=1; j<matrix[0].length; j++) {
				if (matrix[i][0] == 0 || matrix[0][j] == 0) {
					matrix[i][j] = 0;
				}
			}
		}

		if (firstRowZero) {
			for (int i=0; i<matrix[0].length; i++) {
				matrix[0][i] = 0;
			}
		}

		if (firstColumnZero) {
			for (int i=0; i<matrix.length; i++) {
				matrix[i][0] = 0;
			}
		}
	}

	public static void printMatrix(int[][] matrix) {
		for (int i=0; i<matrix.length; i++) {
			for (int j=0; j<matrix[0].length; j++) {
				System.out.print(matrix[i][j]+"  ");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		int[][] matrix = new int[10][10];
		Random rg = new Random();
		for (int i=0; i<10; i++) {
			for (int j=0; j<10; j++) {
				int randomInt = rg.nextInt(20);
				matrix[i][j] = randomInt;
			}
		}
		SetMatrixZeros.printMatrix(matrix);
		SetMatrixZeros inst = new SetMatrixZeros();
		inst.setZeros(matrix);
		System.out.println();
		SetMatrixZeros.printMatrix(matrix);
	}
}