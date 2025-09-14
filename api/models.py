from django.db import models

class FilmeAvaliado(models.Model):
    imdbID = models.CharField(max_length=50)    
    title = models.TextField()
    year = models.DateField(null=True, blank=True)
    img_url = models.TextField()
    #avaliacao = models.ForeignKey(  )

    def __str__(self):
        return self.imdbID
                  
class Avaliacao(models.Model):
    filme = models.ForeignKey(
        FilmeAvaliado, 
        on_delete=models.CASCADE,
        related_name="avaliacoes",
        null=True,
        blank=True
    )
    nota= models.IntegerField()
    comentario=models.TextField()
    
    