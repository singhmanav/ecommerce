// User types
export interface User {
  id: number;
  email: string;
  full_name?: string;
  phone?: string;
  is_admin: boolean;
  is_active: boolean;
  created_at: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  email: string;
  password: string;
  full_name?: string;
  phone?: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

// Product types
export interface Product {
  id: number;
  name: string;
  description?: string;
  price: number;
  category: string;
  sizes: string[];
  colors: string[];
  images: string[];
  stock: number;
  is_active: boolean;
  popularity: number;
  created_at: string;
  updated_at: string;
}

export interface ProductListResponse {
  products: Product[];
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
}

export interface ProductFilters {
  page?: number;
  page_size?: number;
  category?: string;
  min_price?: number;
  max_price?: number;
  size?: string;
  color?: string;
  sort_by?: 'price_asc' | 'price_desc' | 'newest' | 'popularity';
  search?: string;
}

export interface ProductCreate {
  name: string;
  description?: string;
  price: number;
  category: string;
  sizes: string[];
  colors: string[];
  images: string[];
  stock: number;
}

export interface ProductUpdate {
  name?: string;
  description?: string;
  price?: number;
  category?: string;
  sizes?: string[];
  colors?: string[];
  images?: string[];
  stock?: number;
  is_active?: boolean;
}

// Cart types
export interface CartItem {
  product: Product;
  quantity: number;
  selected_size?: string;
  selected_color?: string;
}

export interface Cart {
  items: CartItem[];
  subtotal: number;
  tax: number;
  total: number;
}

// Order types
export interface OrderItem {
  id: number;
  product_id: number;
  product_name: string;
  product_image?: string;
  unit_price: number;
  quantity: number;
  selected_size?: string;
  selected_color?: string;
}

export interface Order {
  id: number;
  user_id: number;
  subtotal: number;
  tax: number;
  total_amount: number;
  status: string;
  shipping_name: string;
  shipping_address_line1: string;
  shipping_address_line2?: string;
  shipping_city: string;
  shipping_state: string;
  shipping_pincode: string;
  shipping_phone: string;
  created_at: string;
  updated_at: string;
}

export interface OrderDetail extends Order {
  items: OrderItem[];
}

export interface OrderListResponse {
  orders: Order[];
  total: number;
}

export interface ShippingAddress {
  shipping_name: string;
  shipping_address_line1: string;
  shipping_address_line2?: string;
  shipping_city: string;
  shipping_state: string;
  shipping_pincode: string;
  shipping_phone: string;
}

export interface OrderItemCreate {
  product_id: number;
  quantity: number;
  selected_size?: string;
  selected_color?: string;
}

export interface OrderCreateRequest {
  items: OrderItemCreate[];
  shipping_address: ShippingAddress;
}

// API Error type
export interface APIError {
  detail: string;
}