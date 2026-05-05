# Inventory management business flow

This file describes the business flow of the inventory management system.

## Create master data

### Unit of measurement

- Unit of measurement for products
- Example: Box, Pc, Kg, etc.

### Set-up UoM for products and variants

- Setup UoM for products and variants
- Partner and Admin user also need to set up UoM for products and variants
- User need to select the UoM for products and variants when creating a new product or variant
- User can not change UoM after product or variant is activated

## Create number of stock for products and variants at first time

- Create number of stock for products and variants at first time
- User need to select the UoM for products and variants when creating a new product or variant

## Inventory Adjustment (Init & Update)

- Admin and Partner can view, create, edit, delete, and submit inventory adjustment requests.
- Allow adding records manually or importing from a template file.
- The template file will be pre-filled with products, variants, and UoM for easier updates.
- Inventory adjustment requests can only be deleted when in draft status.
- Admin must approve the adjustment request to apply the new stock quantities (positive or negative) to on-hand inventory.
- During approval, validate to ensure on-hand inventory does not drop below 0.

## Customer Order & Checkout (Affect)

- Show out-of-stock status on the product marketplace, product details, shopping cart, and checkout page.
- Apply reserved stock logic when a customer successfully checks out and pays for an order.
- Apply unreserved stock logic if the order is canceled while waiting for payment or after successful purchase.

## Return & Refund (Affect)

- When creating a return/refund request, mark which products are returned due to damage and which are not.
- Admin reviews and approves the return/refund request, with the ability to modify the damage status of the products.
- Based on the damage status in the approved return/refund request, decide whether to add the stock back to inventory or not.

## Inventory Reports

- Admin and Partner can view inventory fluctuation reports by product to track transactions affecting inventory (Inventory Adjustments, Purchases, Returns).
- Admin and Partner can view general inventory reports, filtering by category, partner, and date range to see:
  - Opening stock
  - Fluctuations during the period
  - Closing stock
