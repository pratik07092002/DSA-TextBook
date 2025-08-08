fn majority_element(nums: Vec<i32>) -> Vec<i32> {
    let (mut cand1, mut cand2) = (0, 0);
    let (mut count1, mut count2) = (0, 0);

    for &num in &nums {
        if num == cand1 {
            count1 += 1;
        } else if num == cand2 {
            count2 += 1;
        } else if count1 == 0 {
            cand1 = num;
            count1 = 1;
        } else if count2 == 0 {
            cand2 = num;
            count2 = 1;
        } else {
            count1 -= 1;
            count2 -= 1;
        }
    }

    let mut result = Vec::new();
    let n = nums.len();
    let c1_count = nums.iter().filter(|&&x| x == cand1).count();
    let c2_count = nums.iter().filter(|&&x| x == cand2).count();

    if c1_count > n / 3 {
        result.push(cand1);
    }
    if cand2 != cand1 && c2_count > n / 3 {
        result.push(cand2);
    }

    result
}

fn main() {
    println!("{:?}", majority_element(vec![3, 2, 3])); 

}
