using Microsoft.AspNetCore.Mvc;
using ReimbursementAPI.Models;
using ReimbursementAPI.Data;


namespace ReimbursementAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ReceiptsController : ControllerBase
    {
        private readonly AppDbContext _context;
        private readonly string _uploadPath = "Uploads";

        public ReceiptsController(AppDbContext context)
        {
            _context = context;
            Directory.CreateDirectory(_uploadPath);
        }

        [HttpPost("submit")]
        public async Task<IActionResult> Submit([FromForm] ReceiptForm form)
        {
            if (form.ReceiptFile == null || form.ReceiptFile.Length == 0)
                return BadRequest("File is required.");

            var fileName = $"{Guid.NewGuid()}_{form.ReceiptFile.FileName}";
            var filePath = Path.Combine(_uploadPath, fileName);

            using var stream = new FileStream(filePath, FileMode.Create);
            await form.ReceiptFile.CopyToAsync(stream);

            var receipt = new Receipt
            {
                Date = form.Date,
                Amount = form.Amount,
                Description = form.Description,
                FileName = fileName
            };

            _context.Receipts.Add(receipt);
            await _context.SaveChangesAsync();

            return Ok(new { message = "Receipt submitted successfully." });
        }

    }
}
