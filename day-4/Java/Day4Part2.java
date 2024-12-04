import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Day4Part2 {

    public static char[][] readInputAs2DArray(String filePath) throws IOException {
        List<String> lines = new BufferedReader(new FileReader(filePath)).lines().collect(Collectors.toList());
        int maxColumns = lines.stream().mapToInt(String::length).max().orElse(0);
        char[][] array2D = new char[lines.size()][maxColumns];

        for (int i = 0; i < lines.size(); i++) {
            char[] lineChars = lines.get(i).toCharArray();
            System.arraycopy(lineChars, 0, array2D[i], 0, lineChars.length);
            Arrays.fill(array2D[i], lineChars.length, maxColumns, '.');
        }

        return array2D;
    }

    //cell[1]=tr
    //cell[2]=br
    //cell[3]=bl
    static boolean isMAScross(char[] cell) {
        //find 'M's
        List<Integer> indicesM = 
            IntStream.range(0, cell.length)
                .filter(i -> cell[i] == 'M')
                .boxed()
                .collect(Collectors.toList());
        if(indicesM.size()!=2) return false;
        else if((indicesM.get(0)+indicesM.get(1))%2==0) return false;
        else if(cell[(indicesM.get(0)+2)%4]!='S' || cell[(indicesM.get(1)+2)%4]!='S') return false;
        else return true;
    }

    public static int countMAS(char[][] array2D) {
        int count=0;
        int nrows = array2D.length;
        int ncols = array2D[0].length;
        //char c; //center
        //char tl; //top left
        //char tr; //top right
        //char br; //bottom right
        //char bl; //bottom left
        for(int i=1;i<nrows-1;i++){
            for(int j=1;j<ncols-1;j++){
                char c='.', tl='.', tr='.',br='.',bl='.';
                c=array2D[i][j];
                //not valid cell if c is not 'A'
                if(c != 'A') continue;
                if(i-1>=0 && i-1<nrows && j-1>=0 && j-1<ncols) tl=array2D[i-1][j-1];
                if(i-1>=0 && i-1<nrows && j+1>=0 && j+1<ncols) tr=array2D[i-1][j+1];
                if(i+1<nrows && j-1>=0 && j-1<ncols) bl=array2D[i+1][j-1];
                if(i+1<nrows && j+1<ncols) br=array2D[i+1][j+1];
                //'A' found and checking for 2 MAS cross
                if(isMAScross(new char[]{tl,tr,br,bl})) count++;
            }
        }
        return count;
    }

    public static void main(String[] args) throws Exception {
        String inputFilePath = "../day-4.input.txt";
        char[][] array2D = readInputAs2DArray(inputFilePath);
        System.out.println(countMAS(array2D));
    }
}