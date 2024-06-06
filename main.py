from jinja2 import Template 
  
# variables that contain placeholder data 

# Seller Details 
seller_details = {
    "Name": "seller_name",
    "Address": "Seller_Add",
    "PAN_NO": "pan_no",
    "GST": "gst",
    "Place_supply": "place_supply"
}
# Biller Details 
billing_details = {
    "Name": "biller_name",
    "Address1": "Billing_Add1",
    "Address2": "Billing_Add2",
    "Address3": "Billing_Add3",
    "State_Code": "bill_state_code"
}
# Shipping Details 
shipping_details = {
    "Name": "seller_name",
    "Address1": "Shipping_Add1",
    "Address2": "Shipping_Add2",
    "Address3": "Shipping_Add3",
    "State_code": "ship_state_code"
}

# Invoice Details
invoice_details = {
    "Invoice_No": "invoice_no",
    "Invoice_Details": "invoice_details",
    "Invoice_Date": "invoice_data"
} 
# Order Details
order_details = {
    "order_no": "order_no",
    "order_date": "order_date"
}



# Item Details
# net_Amount = unit_Price * Quantity - Discount
item_details1 = {
    "Description": "description of items",
    "Unit_price": 12,
    "Quantity": 5,
    "Discount": 3,
    "Net_amount": 555,  # Unit Price * Quantity - Discount
    "Tax_Type": "CGST",
    "Tax_Amount": 45,
    "Total_Amount": 1023
}

item_details2 = {
    "Description": "description of items",
    "Unit_price": 12,
    "Quantity": 5,
    "Discount": 3,
    "Net_amount": 555,  # Unit Price * Quantity - Discount
    "Tax_Type": "CGST",
    "Tax_Amount": 45,
    "Total_Amount": 1023
}
# Signature Details 

signature_img = "image"

# # Derived Values
# Net_Amount = 
# Tax_Type = 
# Tax_Amount = 
# Total_Amount = 

# Dict of variables
input_list = {"seller_details": {
    "Name": "seller_name",
    "Address": "Seller_Add",
    "PAN_NO": "pan_no",
    "GST": "gst",
    "Place_supply": "place_supply"
} ,
 "billing_details": {
    "Name": "biller_name",
    "Address1": "Billing_Add1",
    "Address2": "Billing_Add2",
    "Address3": "Billing_Add3",
    "State_Code": "bill_state_code"
}, 
"shipping_details": {
    "Name": "seller_name",
    "Address1": "Shipping_Add1",
    "Address2": "Shipping_Add2",
    "Address3": "Shipping_Add3",
    "State_code": "ship_state_code"
},
 "order_details": {
    "order_no": "order_no",
    "order_date": "order_date"
},
 "invoice_details": {
    "Invoice_No": "invoice_no",
    "Invoice_Details": "invoice_details",
    "Invoice_Date": "invoice_data"
} ,
 "item_details": [{
    "Description": "description of items",
    "Unit_price": 12,
    "Quantity": 5,
    "Discount": 3,
    "Net_amount": 555,  # Unit Price * Quantity - Discount
    "Tax_Type": "CGST",
    "Tax_Amount": 45,
    "Total_Amount": 1023
},
{
    "Description": "description of items",
    "Unit_price": 12,
    "Quantity": 5,
    "Discount": 3,
    "Net_amount": 555,  # Unit Price * Quantity - Discount
    "Tax_Type": "CGST",
    "Tax_Amount": 45,
    "Total_Amount": 1023
}], "Signature_img": "signature_img"}

# Create one external form_template html page and read it 
File = open('index.html', 'r') 
content = File.read() 
File.close() 
  
# Render the template and pass the variables 
template = Template(content) 
rendered_form = template.render(input_list) 
    
# save the txt file in the form.html 
output = open('rendered_index.html', 'w') 
output.write(rendered_form) 
output.close() 

# Create PDF file from rendered HTML FILE 
from subprocess import call
html_file_path = "template/index.html"
pdf_file_path  = "output/index.pdf"
call(["wkhtmltopdf", html_file_path, pdf_file_path])