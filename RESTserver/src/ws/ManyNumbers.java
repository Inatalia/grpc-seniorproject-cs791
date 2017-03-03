package ws;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

import java.io.IOException;

import java.nio.file.Files;
import java.nio.file.Paths;
 
@Path("/numbers")
public class ManyNumbers {

        // recieves numbers from client
        @POST
	@Produces(MediaType.TEXT_PLAIN)
	public String returnBook(String request){
           System.out.println(request);
    	   return "Success";
   	}
}
