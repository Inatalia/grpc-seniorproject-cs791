package ws;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

import java.io.IOException;

import java.nio.file.Files;
import java.nio.file.Paths;
 
@Path("/container")
public class ContainerPicture {

        // only build this array once
        private static byte[] picture;
        static{
            try{
            picture = Files.readAllBytes(Paths.get("/Users/warren/Desktop/grpc-seniorproject-cs791/data/containers.jpg"));
            }
            catch(IOException e){
                System.err.println(e);
                System.err.println("Error locating file -- check path.");
            }
        }

        // just return image as a byte array
        @GET
	@Produces(MediaType.TEXT_PLAIN)
	public byte[] returnPicture(){
    	   return ContainerPicture.picture;
   	}
}
