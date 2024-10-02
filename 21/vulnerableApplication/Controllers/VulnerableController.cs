using System.IO;
using System.Xml.Serialization;
using Microsoft.AspNetCore.Mvc;

namespace VulnerableApp.Controllers
{
    public class VulnerableController : Controller
    {
        [HttpGet("/serialize")]
        public IActionResult SerializedObject()
        {
            var obj = new VulnerableData { Name = "John Doe", Age = 30 };
            var xmlSerializer = new XmlSerializer(obj.GetType());

            using (var stringWriter = new StringWriter())
            {
                xmlSerializer.Serialize(stringWriter, obj);
                return Content(stringWriter.ToString(), "application/xml");
            }
        }
    }

    public class VulnerableData
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }
}
