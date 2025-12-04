# CivicGuard
### Community Incident Reporting & Transparency Platform (SDG 16)

CivicGuard is a web-based platform designed to strengthen community trust in institutions through transparent reporting, tracking, and resolution of public incidents. This system empowers citizens to submit incidents, allows administrators to manage and resolve them, and provides a public transparency dashboard aligned with **Sustainable Development Goal 16 – Peace, Justice & Strong Institutions**.

---

## Project Overview

CivicGuard enables:

- Citizens to report incidents securely.
- Admins to review, update, and resolve incidents.
- The public to track how incidents are handled.
- Institutions to demonstrate transparency and accountability.

Incidents move through three workflow stages:

1. **Pending** – Submitted and awaiting admin review  
2. **Reviewed** – Verified and being processed  
3. **Solved** – Final report published for public viewing  

The platform includes:

- A custom admin dashboard  
- Full CRUD incident management  
- Public transparency dashboard  
- Secure admin authentication  
- Clean minimalist frontend and institutional styling  

---

## Current Features (Completed)

### **1. Project Setup & Core Structure**
- Django project initialized (`civicguard`)
- `incidents` app created
- Bootstrap 5 integrated for UI
- Fully responsive base layout
- Home page & About page created (institutional theme)

---

### **2. Incident Model**
A complete model with fields for:

- User information  
- Incident type, description, location  
- Evidence file upload  
- Auto-generated reference ID  
- Admin review workflow  
- Admin notes & public report  
- Status tracking  
- Automatic timestamps  

---

### **3. User Incident Submission System**
- Clean, minimalist, responsive form  
- Evidence upload support  
- Form validation  
- Thank-you page  
- Saves incident to the database  

---

### **4. Custom Admin Authentication**
- Custom admin login page (no public registration)  
- Django session authentication  
- Admin-only protected pages  
- Custom logout system  

---

### **5. Admin Dashboard (Backend UI)**
Includes:

- Sidebar navigation  
- Overview KPIs  
  - Total incidents  
  - Pending  
  - Reviewed  
  - Solved  
- Analytics section (Chart.js)  
  - Status distribution chart  
  - Category distribution chart  

---

### **6. Admin Incident Management (CRUD)**
#### Manage Incidents Table  
- Responsive admin table  
- Status badges  
- View / Edit / Delete actions  

#### Incident Detail Page  
- Full incident information  
- User details  
- Evidence preview  
- Admin notes + public report  
- Status update section  

#### Edit Incident Page  
- Full editable form for all incident fields  
- Evidence replacement option  

#### Delete Incident  
- Confirmation screen  
- Secure deletion  
- Redirect to incident list  

#### Add Incident (Admin)  
- Admin can manually create incidents  
- Useful for phone/in-person reports  

---

### **7. Public Transparency Dashboard**
Accessible to all users:

- `/incidents/` lists incidents grouped by:
  - Pending
  - Reviewed
  - Solved
- Clean blog-style layout
- Shows summaries, statuses, and timestamps

### **Public Incident Detail Page**
- Full incident description  
- Status badge  
- Evidence link (if available)  
- Admin’s final public report (when solved)  

This fulfills the transparency goal of SDG 16.

---




