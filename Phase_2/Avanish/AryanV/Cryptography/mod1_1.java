public class mod1_1
{
    public static void main(String args [])
    {
        int arr [] = {350 ,63 ,353 ,198 ,114 ,369,346 ,184 ,202, 322 ,94 ,235, 114 ,110, 185, 188 ,225, 212, 366, 374, 261, 213 };
        for(int i = 0;i<arr.length;i++)
        {
            arr[i] = arr[i]%37;
        }
        char dec [] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_'};
        for(int j = 0; j<arr.length;j++)
        {
            System.out.print(dec[(arr[j])]);
        }
    }
}