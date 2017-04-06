boolean stringsRearrangement(String[] inputArray) {

  class Helper {
    String[] inputArray;

    void swap(int i, int j) {
      String tmp = inputArray[i];
      inputArray[i] = inputArray[j];
      inputArray[j] = tmp;
    }

    boolean bruteForce(int depth) {
      if (depth == inputArray.length) {
        boolean correct = true;
        for (int i = 0; i < inputArray.length - 1; i++) {
          int differences = 0;
          for (int j = 0; j < inputArray[i].length(); j++) {
            if (inputArray[i].charAt(j) != inputArray[i + 1].charAt(j)) {
              differences++;
            }
          }
          correct &= (differences == 1);
        }
        if (correct) {
          return true;
        }
        return false;
      }
      for (int i = depth; i < inputArray.length; i++) {
        swap(depth, i);
        if 	(bruteForce(depth + 1)) {
          return true;
        }
        swap(depth, i);
      }
      return false;
    }
  };

  Helper h = new Helper();
  h.inputArray = inputArray;

  if (h.bruteForce(0)) {
    return true;
  }
  return false;
}