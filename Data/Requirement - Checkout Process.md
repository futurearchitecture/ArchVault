Tags: #Requirements/Functional #User_Story #Example 
Links: [[eCommerce Website Example - Functional Requirements]]


As a customer ready to complete my purchase on the ecommerce website, I want to be able to easily and securely checkout so that I can receive my products in a timely manner. I expect to be able to select my preferred shipping and delivery options, and to see the estimated delivery date and shipping costs. I also expect to be able to securely provide my billing and payment information, including the option to save my payment information for future purchases. Additionally, I expect to receive a detailed order summary with an order number and confirmation of my purchase, including any applicable discounts or promotions. Finally, I expect to be able to receive updates on my order status, including shipping and delivery updates, via email or SMS.


## Flowchart
```mermaid
flowchart LR
  subgraph "Customer"
    C1((Choose Shipping and Payment Method))
    C2((Enter Shipping and Billing Information))
    C3((Review and Confirm Order))
  end

  subgraph "Ecommerce Website"
    W1((Process Shipping and Payment Method))
    W2((Process Shipping and Billing Information))
    W3((Process Order))
    W4((Send Order Confirmation))
  end

  subgraph "Logistics Provider"
    L1((Process Shipping))
    L2((Send Shipping Confirmation))
  end

  C1 --> W1
  C2 --> W2
  C3 --> W3
  W3 --> W4
  W1 --> L1
  L1 --> L2

```


## Sequence Diagram
```mermaid
sequenceDiagram
  participant Customer
  participant EcommerceWebsite
  participant LogisticsProvider

  Customer->>EcommerceWebsite: Choose Shipping and Payment Method
  Customer->>EcommerceWebsite: Enter Shipping and Billing Information
  Customer->>EcommerceWebsite: Review and Confirm Order
  EcommerceWebsite->>LogisticsProvider: Process Shipping
  LogisticsProvider->>EcommerceWebsite: Send Shipping Confirmation
  EcommerceWebsite->>Customer: Send Order Confirmation

```
