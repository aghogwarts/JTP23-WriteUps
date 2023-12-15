public class mod2_1 {
    public static void main(String args[])
    {
        int arr[] ={28, 14, 22 ,30 ,18, 32, 30 ,12 ,25, 37, 8 ,31, 18, 4, 37, 4 ,1 ,4,1 ,1 ,3 ,1, 1 };
        char dec [] = {' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_'};
        for(int j = 0; j<arr.length;j++)
        {
            System.out.print(dec[(arr[j])]);
        }
    }
}
