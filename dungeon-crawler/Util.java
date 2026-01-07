/* Util
 * used for its random integer generator method, randint
 */

class Util{
  public static int randint(int a, int b){
    return (int)(Math.random()*(b-a+1)+a);
  }

}
