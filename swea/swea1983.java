package swea;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea1983 {
    public static void main(String[] args) throws IOException{
        String[] grade = {"A+","A0","A-","B+","B0","B-","C+","C0","C-",
        "D0"};
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        int tc = Integer.parseInt(br.readLine());

        for(int t =1 ;t<tc+1; t++)
        {
            st = new StringTokenizer(br.readLine()," ");
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            double[] result = new double[N+1];
            for (int i =1;i<=N;i++)
            {
                st = new StringTokenizer(br.readLine()," ");
                int middle_ex = Integer.parseInt(st.nextToken());
                int final_ex = Integer.parseInt(st.nextToken());
                int assignment = Integer.parseInt(st.nextToken());
                double sum = 0.35 * middle_ex + 0.45 * final_ex + assignment * 0.20;
                result[i] = sum;
                
            }
            int cnt=0;
            for (int i =1;i<=N;i++)
            {
                if (result[i] > result[K]) cnt++;

            }
            System.out.printf("#%d %s\n", t,grade[cnt/(N/10)]);


        }
        

        
    }
}
