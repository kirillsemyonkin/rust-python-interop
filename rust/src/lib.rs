// ensure explicit `unsafe {}`
#![deny(unsafe_op_in_unsafe_fn)]

use core::slice;

#[no_mangle]
pub unsafe extern "C" fn selection_sort(arr: *mut u64, len: usize) {
    // move from unsafe pointer world to safe Rust slices
    let arr = unsafe { slice::from_raw_parts_mut(arr, len) };
    
    for j in 0..len - 1 {
        let mut min_v = arr[j];
        let mut min_i = j;
        for i in j + 1..len {
            if arr[i] < min_v {
                min_v = arr[i];
                min_i = i;
            }
        }
        arr.swap(j, min_i)
    }
}
