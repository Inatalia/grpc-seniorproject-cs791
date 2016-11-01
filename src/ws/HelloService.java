package ws;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

//@Path("/hello")
public class HelloService {

  @GET
    @Path("/intextform")
    @Produces(MediaType.TEXT_PLAIN)
    public String helloWorld(){
      return "Hello World!";

    }
  @GET
    @Path("/intextform2")
    @Produces(MediaType.TEXT_PLAIN)
    public String helloWorld2(){
      return "Hello World2!";

    }

  @Path("hello")
    public class HelloWorldResource {
      @GET
        @Produces(MediaType.TEXT_PLAIN)
        public String sayhello() {
          return "hello";
        }

    }
}
