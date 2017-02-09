package ws;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

import java.io.IOException;

import java.nio.file.Files;
import java.nio.file.Paths;
 
@Path("/paradise")
public class ParadiseLost {

        // only build this string once
        private static String book;
        static{
            try{
            book = new String(Files.readAllBytes(Paths.get("/Users/warren/Desktop/grpc-seniorproject-cs791/data/paradiseLost.txt")));
            }
            catch(IOException e){
                System.err.println(e);
                System.err.println("Error locating file -- check path.");
            }
        }

        // just return good ole Paradise Lost
        @GET
	@Produces(MediaType.TEXT_PLAIN)
	public String returnBook(){
    	   return ParadiseLost.book;
   	}
}
