#include<bits/stdc++.h>
using namespace std;
int maxSumSubArray(int arr[], int n)
{
    int maxsum=0;
    int cursum=0;
    for(int i=0;i<n;i++){
        cursum = cursum + arr[i];
        if(cursum > maxsum){
            maxsum = cursum;
        }
        if(cursum<0)
        cursum = 0;
    }
return maxsum;
}
int main()
{
    int arr[] = {-2, -3, 4, -1, -2, 1, 5, -3};
    int n = sizeof(arr)/sizeof(arr[0]);
    int max_sum = maxSumSubArray(arr, n);
    cout << "Maximum contiguous sum is " << max_sum;
    return 0;
}
