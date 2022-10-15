public class firstLast {
    public static void main(String[] args) {
        int[] arr={5,7,7,8,8,10};
        int target=7;

    }
    static int binarySearch(int[] arr,int target){
        int start=0;
        int end=arr.length-1;
        while(start<=end){
            int mid=start+(end-start)/2;
            if(target>arr[mid]){
                start=mid+1;
            }
            else if(target<arr[mid]){
                end=mid-1;
            }
            else{
                return mid;
            }
        }
        return -1;

    }
    static int search(int[] arr,int target,boolean hy){

        return target;
    }
}
