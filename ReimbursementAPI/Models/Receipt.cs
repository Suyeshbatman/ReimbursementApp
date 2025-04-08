using Microsoft.AspNetCore.Http;

namespace ReimbursementAPI.Models
{
    public class Receipt
    {
        public int Id { get; set; }
        public DateTime Date { get; set; }
        public decimal Amount { get; set; }
        public string Description { get; set; } = string.Empty;
        public string FileName { get; set; } = string.Empty;
    }
}
