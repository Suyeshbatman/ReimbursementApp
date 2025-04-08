import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-receipt-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './receipt-form.component.html',
  styleUrls: ['./receipt-form.component.scss']
})
export class ReceiptFormComponent {
  form: FormGroup;
  file: File | null = null;
  message = '';

  constructor(private fb: FormBuilder, private http: HttpClient) {
    // Initialize the form with validation
    this.form = this.fb.group({
      date: ['', Validators.required],
      amount: ['', [Validators.required, Validators.min(0)]],
      description: ['', Validators.required]
    });
  }

  // Method to handle file input
  onFileChange(event: any) {
    this.file = event.target.files[0];
  }

  // Method to submit the form
  submit() {
    if (!this.file) {
      this.message = 'Please attach a receipt file.';
      return;
    }

    // Create FormData to send the form data along with the file
    const formData = new FormData();
    formData.append('date', this.form.value.date);
    formData.append('amount', this.form.value.amount);
    formData.append('description', this.form.value.description);
    formData.append('receiptFile', this.file);

    // Make the HTTP POST request to the backend API
    this.http.post('http://localhost:5100/api/receipts/submit', formData)
      .subscribe({
        next: () => this.message = 'Receipt submitted successfully!',
        error: () => this.message = 'Error submitting receipt.'
      });
  }
}
