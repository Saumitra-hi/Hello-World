#include<bits/stdc++.h>
using namespace std;
int CountTriplet(int arr[], int n)
{
    int count = 0;
    if(n<3)
    {
        return 0;
    }
    if(n == 3)
    {
        if(arr[0]==arr[1]+arr[2]){
            count++;
        }
        if(arr[1] == arr[0] + arr[2]){
            count++;
        }
        if(arr[2] == arr[0] + arr[1]){
            count++;
        }
        return count;
    }
    sort(arr,arr+n);
    for(int i=n-1; i>=0; i--){
        int left = 0, right = i-1;
        while(left<right){
            if(arr[left]+arr[right] == arr[i]){
                count++;
                left++;
                right--;
                //break;
            }
            else if(arr[left] + arr[right] < arr[i]){
                left++;
            }
            else{
                right--;
            }
        }
    }
    return count;
}