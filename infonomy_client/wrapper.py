import requests
from infonomy_client import ApiClient, Configuration
from infonomy_client.api import (
    AuthApi,
    BotSellersApi, 
    DecisionContextsApi,
    InboxApi,
    InspectionApi,
    ProfilesApi,
    UsersApi
)

class InfonomyClient:

    def __init__(self, username: str, email: str, password: str, base_url: str = "http://localhost:8000"):
        self.username = username
        self.email = email
        self.password = password
        self.base_url = base_url

        # Create shared configuration
        self.config = Configuration(host=base_url)
        self.api_client = None
        self.access_token = None
        
        # Initialize all API instances as None (lazy loading)
        self._auth_api = None
        self._bot_sellers_api = None
        self._decision_contexts_api = None
        self._default_api = None
        self._inbox_api = None
        self._inspection_api = None
        self._profiles_api = None
        self._users_api = None
    
    def register(self):
        response = requests.post(f"{self.base_url}/api/auth/register", json={"username": self.username, "email": self.email, "password": self.password})
        print(f"Registration of {self.username}: {response.status_code}")
        return response.status_code

    def login(self):
        response = requests.post(f"{self.base_url}/api/auth/jwt/login", data={"username": self.email, "password": self.password})
        self.access_token = response.json()["access_token"]
        self._refresh_apis()
        print(f"Login of {self.email}: {response.status_code}")
        return self.access_token

    def logout(self):
        """Clear authentication"""
        self.access_token = None
        self._refresh_apis()
    
    # def _create_api_client(self):
    #     """Create ApiClient with current configuration"""
    #     if self.access_token:
    #         # Method 2: Set access token on configuration
    #         self.config.access_token = self.access_token
    #         # Alternative: Set it in default headers
    #         # self.config.api_key['Authorization'] = f'Bearer {self.access_token}'
        
    #     return ApiClient(self.config)

    def _create_api_client(self):
        client = ApiClient(self.config)
        
        if self.access_token:
            # Set the header directly on the client using set_default_header
            client.set_default_header('Authorization', f'Bearer {self.access_token}')
            print(f"Set Authorization header directly on client: Bearer {self.access_token}...")
        
        return client

    # def _create_api_client(self):
    #     if self.access_token:
    #         if not hasattr(self.config, 'api_key'):
    #             self.config.api_key = {}
    #         self.config.api_key['Authorization'] = f'Bearer {self.access_token}'
            
    #         # Debug: print the actual configuration
    #         print(f"Base URL: {self.config.host}")
    #         print(f"API Keys: {getattr(self.config, 'api_key', {})}")
    #         print(f"Access Token: {self.access_token[:20]}..." if self.access_token else "None")
        
    #     # Create the client and add a debug interceptor
    #     client = ApiClient(self.config)
        
    #     # Debug: let's see what URLs are actually being called
    #     original_call_api = client.call_api
    #     def debug_call_api(*args, **kwargs):
    #         print(f"OpenAPI client calling: {args}")
    #         print(f"With kwargs: {kwargs}")
    #         # Also print the actual headers being sent
    #         if 'headers' in kwargs:
    #             print(f"Headers being sent: {kwargs['headers']}")
    #         return original_call_api(*args, **kwargs)
        
    #     client.call_api = debug_call_api
        
    #     return client

    # def _create_api_client(self):
    #     if self.access_token:
    #         if not hasattr(self.config, 'api_key'):
    #             self.config.api_key = {}
    #         self.config.api_key['Authorization'] = f'Bearer {self.access_token}'
        
    #     # Debug: print the actual configuration
    #     print(f"Base URL: {self.config.host}")
    #     print(f"API Keys: {getattr(self.config, 'api_key', {})}")
        
    #     # Create the client and add a debug interceptor
    #     client = ApiClient(self.config)
        
    #     # Debug: let's see what URLs are actually being called
    #     original_call_api = client.call_api
    #     def debug_call_api(*args, **kwargs):
    #         print(f"OpenAPI client calling: {args}")
    #         print(f"With kwargs: {kwargs}")
    #         return original_call_api(*args, **kwargs)
        
    #     client.call_api = debug_call_api
        
    #     return client

    def _refresh_apis(self):
        """Refresh all API instances with new authentication"""
        # Create new API client with updated config
        self.api_client = self._create_api_client()
        
        # Reset all API instances so they get recreated with new auth
        self._auth_api = None
        self._bot_sellers_api = None
        self._decision_contexts_api = None
        self._default_api = None
        self._inbox_api = None
        self._inspection_api = None
        self._profiles_api = None
        self._users_api = None

    # Property-based API access (lazy loading)
    @property
    def auth(self) -> AuthApi:
        """Access to authentication API"""
        if self._auth_api is None:
            if self.api_client is None:
                self.api_client = self._create_api_client()
            self._auth_api = AuthApi(self.api_client)
        return self._auth_api
    
    @property
    def profiles(self) -> ProfilesApi:
        """Access to profiles API (buyers/sellers)"""
        if self._profiles_api is None:
            if self.api_client is None:
                self.api_client = self._create_api_client()
            self._profiles_api = ProfilesApi(self.api_client)
        return self._profiles_api
    
    @property
    def decision_contexts(self) -> DecisionContextsApi:
        """Access to decision contexts API"""
        if self._decision_contexts_api is None:
            if self.api_client is None:
                self.api_client = self._create_api_client()
            self._decision_contexts_api = DecisionContextsApi(self.api_client)
        return self._decision_contexts_api
    
    @property
    def bot_sellers(self) -> BotSellersApi:
        """Access to bot sellers API"""
        if self._bot_sellers_api is None:
            if self.api_client is None:
                self.api_client = self._create_api_client()
            self._bot_sellers_api = BotSellersApi(self.api_client)
        return self._bot_sellers_api
    
    @property
    def inbox(self) -> InboxApi:
        """Access to inbox API"""
        if self._inbox_api is None:
            if self.api_client is None:
                self.api_client = self._create_api_client()
            self._inbox_api = InboxApi(self.api_client)
        return self._inbox_api
    
    @property
    def inspection(self) -> InspectionApi:
        """Access to inspection API"""
        if self._inspection_api is None:
            if self.api_client is None:
                self.api_client = self._create_api_client()
            self._inspection_api = InspectionApi(self.api_client)
        return self._inspection_api
    
    @property
    def users(self) -> UsersApi:
        """Access to users API"""
        if self._users_api is None:
            if self.api_client is None:
                self.api_client = self._create_api_client()
            self._users_api = UsersApi(self.api_client)
        return self._users_api
        
    # Context manager support
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, 'api_client') and self.api_client:
            # Clean up API client if it has cleanup methods
            pass
