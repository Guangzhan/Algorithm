package guet.edu.cn;

public class Algorithm
{
	
	public static void main(String[] args)
	{
		getSum();
	}
	/**
	 * 对于100n^2和2^n两个算法进行比较，我们可以这样做：对100n^2-2^n操作，如果结果小于0，那么此时的n就是我们所求的值。
	 * java中求一个数的n次方，方法为Math.pow(x,y);即x的y次方
	 */
	public static void getSum()
	{
		int n = 2;
		long sum = 0;
		boolean flag = true;
		while (flag)
		{
			sum = (long) (64 * n * Algorithm.log(n, 2) - 8 * Math.pow(n, 2));
			System.out.println("第" + n + "次计算结果为：" + sum);
			if (sum < 0)
			{
				flag = false;
				break;
			}
			n = n + 1;
		}
		System.out.println(n);
	}

	public static double log(double value, double base)
	{
		return Math.log(value) / Math.log(base);
	}

}
