import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.util.CoreMap;

import java.util.*;
import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.nio.file.Files;
import java.nio.file.*;

import static java.nio.file.StandardCopyOption.*;


public class Main {
    public static void main(String[] args) throws IOException {

        // read file with keywords to be searched in captions
        File keywords = new File("data/keywords");
        BufferedReader keywords_reader = new BufferedReader(new FileReader(keywords));
        String keyword;
        List<String> keywordList = new ArrayList<>();

        // create empty folders each keyword
        while ((keyword = keywords_reader.readLine()) != null) {
            File dir = new File("data/filtered_data/" + keyword);
            boolean mkdir = dir.mkdir();
            keywordList.add(keyword);
        }

        // creates a StanfordCoreNLP object, with POS tagging, lemmatization
        Properties props = new Properties();
        props.setProperty("annotators", "tokenize, ssplit, pos, lemma");
        StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

        // reading caption file
        File captions = new File("data/caption");
        BufferedReader caption_reader = new BufferedReader(new FileReader(captions));
        String caption;

        while ((caption = caption_reader.readLine()) != null) {

            // create an empty Annotation just with the given text
            Annotation document = new Annotation(caption);

            // run all Annotators on this text
            pipeline.annotate(document);

            // these are all the sentences in this document
            // a CoreMap is essentially a Map that uses class objects as keys and has values with custom types
            List<CoreMap> sentences = document.get(CoreAnnotations.SentencesAnnotation.class);
            for (CoreMap sentence : sentences) {

                // traversing the words in the current sentence
                // a CoreLabel is a CoreMap with additional token-specific methods
                for (CoreLabel token : sentence.get(CoreAnnotations.TokensAnnotation.class)) {

                    // this is the POS tag of the token
                    String lemma = token.get(CoreAnnotations.LemmaAnnotation.class);

                    // if lemma is in keywordList
                    if (keywordList.contains(lemma)) {
                        System.out.println(caption);
                        System.out.println("Lemma Annotation");
                        System.out.println(token + ":" + lemma);
                        System.out.println("------------------------------------------------------");
                        Pattern pattern = Pattern.compile("[0-9]*.jpg");
                        Matcher matcher = pattern.matcher(caption);

                        // copy the image to the created folder
                        if (matcher.find()) {
                            Path temp = Files.copy(Paths.get("data/flickr30k_images/" + matcher.group(0)),
                                    Paths.get("data/filtered_data/" + lemma + "/" + matcher.group(0)),
                                    REPLACE_EXISTING);
                        }
                    }
                }
            }
        }

        // print number of images in each folder
        System.out.println("Image Statistics: ");
        for (String s : keywordList) {
            File directory = new File("data/filtered_data/" + s);
            int fileCount = Objects.requireNonNull(directory.list()).length;
            System.out.println(s + ":" + fileCount);
        }

    }
}
