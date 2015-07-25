public class JumpGame2 {
	public int jump(int[] nums) {

		if (nums == null || nums.length == 0) {
			return 0;
		}

		int lastReach = 0;
		int reach = 0;
		int step = 0;

		for (int i = 0; i <= reach && i < nums.length; i++) {

			if (i > lastReach) {
				step++;
				lastReach = reach;
			}
			reach = Math.max(reach, nums[i]+i);
		}
		if (reach < nums.length-1) {
			return 0;
		}

		return step;
	}

	public static void main(String[] args) {
		int[] arr = {2, 3, 1, 1, 4};
		JumpGame2 jg = new JumpGame2();
		System.out.println(jg.jump(arr));
	}
}