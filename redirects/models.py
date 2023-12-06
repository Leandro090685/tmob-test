import logging
from django.db import models
from django.forms.models import model_to_dict
from django.core.cache import cache
from django.db.models.signals import post_save

logger = logging.getLogger(__name__)

class Redirect(models.Model):
    key = models.CharField(max_length=128)
    url = models.URLField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def get_redirect(self):
        result = cache.get(self.key)
        if result:
            return {
            "key": result.get('key'),
            "url": result.get('url')
            }
        else:
            return None
        
    @property    
    def get_redirect_db(self):
        try:
            redirect_obj = Redirect.objects.get(key=self.key, active=True)
            return {
                "key": redirect_obj.key,
                "url": redirect_obj.url,
                "location":"database"
            }
        except Redirect.DoesNotExist:
            return None
        
def receiver(sender, instance:Redirect, **kwargs):
    if instance.active:
        logger.info(f"instance create in active with key={instance.key}")
        # cache.set(instance.key, model_to_dict(instance))
        cache.set(instance.key, {'key': instance.key, 'url': instance.url}) # Me parece mejor asi si solo necesito key y url

post_save.connect(receiver, sender=Redirect)
