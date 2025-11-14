import { apiClient, setToken, removeToken } from './api-client';
import {
  User,
  LoginRequest,
  RegisterRequest,
  AuthResponse,
  Product,
  ProductListResponse,
  ProductFilters,
  ProductCreate,
  ProductUpdate,
  Order,
  OrderDetail,
  OrderListResponse,
  OrderCreateRequest,
  CartItem,
} from '@/types';

// Auth API
export const authAPI = {
  register: async (data: RegisterRequest): Promise<User> => {
    return apiClient.post<User>('/auth/register', data);
  },

  login: async (data: LoginRequest): Promise<AuthResponse> => {
    const response = await apiClient.post<AuthResponse>('/auth/login', data);
    setToken(response.access_token);
    return response;
  },

  logout: (): void => {
    removeToken();
  },

  getCurrentUser: async (): Promise<User> => {
    return apiClient.get<User>('/auth/me');
  },
};

// Products API
export const productsAPI = {
  list: async (filters?: ProductFilters): Promise<ProductListResponse> => {
    return apiClient.get<ProductListResponse>('/products', filters);
  },

  get: async (id: number): Promise<Product> => {
    return apiClient.get<Product>(`/products/${id}`);
  },
};

// Orders API
export const ordersAPI = {
  create: async (data: OrderCreateRequest): Promise<OrderDetail> => {
    return apiClient.post<OrderDetail>('/orders', data);
  },

  list: async (): Promise<OrderListResponse> => {
    return apiClient.get<OrderListResponse>('/orders');
  },

  get: async (id: number): Promise<OrderDetail> => {
    return apiClient.get<OrderDetail>(`/orders/${id}`);
  },
};

// Admin API
export const adminAPI = {
  // Products
  createProduct: async (data: ProductCreate): Promise<Product> => {
    return apiClient.post<Product>('/admin/products', data);
  },

  updateProduct: async (id: number, data: ProductUpdate): Promise<Product> => {
    return apiClient.put<Product>(`/admin/products/${id}`, data);
  },

  deleteProduct: async (id: number): Promise<void> => {
    return apiClient.delete<void>(`/admin/products/${id}`);
  },

  // Orders
  listOrders: async (): Promise<OrderListResponse> => {
    return apiClient.get<OrderListResponse>('/admin/orders');
  },

  getOrder: async (id: number): Promise<OrderDetail> => {
    return apiClient.get<OrderDetail>(`/admin/orders/${id}`);
  },
};

// Cart helper functions (local storage)
const CART_KEY = 'shopping_cart';

export const cartAPI = {
  getCart: (): CartItem[] => {
    if (typeof window === 'undefined') return [];
    const cart = localStorage.getItem(CART_KEY);
    return cart ? JSON.parse(cart) : [];
  },

  setCart: (items: CartItem[]): void => {
    localStorage.setItem(CART_KEY, JSON.stringify(items));
  },

  addItem: (item: CartItem): void => {
    const cart = cartAPI.getCart();
    const existingIndex = cart.findIndex(
      (i) =>
        i.product.id === item.product.id &&
        i.selected_size === item.selected_size &&
        i.selected_color === item.selected_color
    );

    if (existingIndex >= 0) {
      cart[existingIndex].quantity += item.quantity;
    } else {
      cart.push(item);
    }

    cartAPI.setCart(cart);
  },

  updateQuantity: (index: number, quantity: number): void => {
    const cart = cartAPI.getCart();
    if (quantity <= 0) {
      cart.splice(index, 1);
    } else {
      cart[index].quantity = quantity;
    }
    cartAPI.setCart(cart);
  },

  removeItem: (index: number): void => {
    const cart = cartAPI.getCart();
    cart.splice(index, 1);
    cartAPI.setCart(cart);
  },

  clearCart: (): void => {
    localStorage.removeItem(CART_KEY);
  },

  getCartTotal: (): { subtotal: number; tax: number; total: number } => {
    const cart = cartAPI.getCart();
    const subtotal = cart.reduce((sum, item) => sum + item.product.price * item.quantity, 0);
    const tax = subtotal * 0.18; // 18% tax
    const total = subtotal + tax;
    return { subtotal, tax, total };
  },
};