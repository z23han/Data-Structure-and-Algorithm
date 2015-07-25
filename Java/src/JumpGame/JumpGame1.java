public class JumpGame1 {
	public boolean canJump(int[] A) {
		if (A.length <= 1) {
			return true;
		}

		int max = A[0];

		for (int i = 0; i < A.length; i++) {
			if (max <= i && A[i] == 0) {
				return false;
			}

			if (i + A[i] > max) {
				max = i + A[i];
			}

			if (max >= A.length-1) {
				return true;
			}
		}

		return false;
	}

	public static void main(String[] args) {
		int[] arr1 = {2, 3, 1, 1, 4};
		int[] arr2 = {3, 2, 1, 0, 4};

		JumpGame1 jg = new JumpGame1();
		System.out.println(jg.canJump(arr1));
		System.out.println(jg.canJump(arr2));
	}
}