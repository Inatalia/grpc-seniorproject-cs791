package ws;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

@Path("helloService")
public class HelloService {

  @Path("hello")
    public class HelloWorldResource {
        @GET
        @Produces(MediaType.TEXT_PLAIN)
        public String sayhello() {
          return "hello";
        }

    }
}
