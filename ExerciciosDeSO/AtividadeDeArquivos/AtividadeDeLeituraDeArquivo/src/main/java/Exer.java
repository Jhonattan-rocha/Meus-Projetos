import java.io.*;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

public class Exer {
    public static void main(String[] args) throws IOException {
        String diretorio = "C:\\Users\\User\\Documents\\TEMP";
        File arquivo = new File("generic_food.csv");
        Charset charset = StandardCharsets.UTF_8;

        if (validarDiretorioEArquivo(diretorio, arquivo.getName(), "TEMP")){
            lerCVS(new File(diretorio+"\\"+arquivo.getName()), charset);
        }
    }

    public static boolean validarDiretorioEArquivo(String diretorio, String csv, String validar) {
        File dir = new File(diretorio);
        boolean arquivo = false;
        boolean pasta = diretorio.contains(validar);
        if (dir.exists() && dir.isDirectory()) {
            File[] lista = dir.listFiles();
            assert lista != null;
            for (File arq : lista) {
                if (arq.isFile()) {
                    if (arq.getName().contains(csv)) {
                        arquivo = true;
                    }
                }
            }
        } else {
            return false;
        }
        return arquivo && pasta;
    }

    private static void lerCVS(File arq, Charset charset) throws IOException {
        FileInputStream abreArquivo = new FileInputStream(arq);
        InputStreamReader leARquivo = new InputStreamReader(abreArquivo, charset);
        BufferedReader buffer = new BufferedReader(leARquivo);
        String linha = buffer.readLine();
        StringBuilder stringBuilder = new StringBuilder();
        while (linha != null) {
            String[] nomes = linha.split(",");
            if (nomes[2].contains("Fruits")){
                String texto = String.valueOf(stringBuilder.append(nomes[0]).append("      ").append(nomes[1]).append("      ").append(nomes[3]));
                System.out.println(texto);
                stringBuilder.setLength(0);
            }
            linha = buffer.readLine();
        }
        buffer.close();
        leARquivo.close();
        abreArquivo.close();
    }
}
