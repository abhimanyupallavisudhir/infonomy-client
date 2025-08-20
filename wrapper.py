import requests
from infonomy_client import ApiClient, Configuration
from infonomy_client.api import (
    AuthApi,
    BotSellersApi, 
    DecisionContextsApi,
    DefaultApi,
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
        response = requests.post(f"{self.base_url}/auth/register", json={"username": self.username, "email": self.email, "password": self.password})
        print(f"Registration of {self.username}: {response.status_code}")
        return response.status_code

    def login(self):
        response = requests.post(f"{self.base_url}/auth/jwt/login", data={"username": self.email, "password": self.password})
        self.access_token = response.json()["access_token"]
        self._refresh_apis()
        print(f"Login of {self.email}: {response.status_code}")
        return self.access_token

    def logout(self):
        """Clear authentication"""
        self.access_token = None
        self._refresh_apis()
    
    def _create_api_client(self):
        """Create ApiClient with current configuration"""
        if self.access_token:
            # Method 2: Set access token on configuration
            self.config.access_token = self.access_token
            # Alternative: Set it in default headers
            # self.config.api_key['Authorization'] = f'Bearer {self.access_token}'
        
        return ApiClient(self.config)
    
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
    
    @property
    def default(self) -> DefaultApi:
        """Access to default API"""
        if self._default_api is None:
            if self.api_client is None:
                self.api_client = self._create_api_client()
            self._default_api = DefaultApi(self.api_client)
        return self._default_api
    
    # Context manager support
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, 'api_client') and self.api_client:
            # Clean up API client if it has cleanup methods
            pass
