using Microsoft.AspNetCore.Mvc;

namespace VulnerableApp.Controllers
{
    public class KeyController : Controller
    {
        [HttpGet("/private-key")]
        public IActionResult ExposePrivateKey()
        {
            // Reading and exposing the private key from the file
            string privateKey = System.IO.File.ReadAllText("wwwroot/keys/privatekey.pem");
            return Content(privateKey, "text/plain");
        }
    }
}
