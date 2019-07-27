from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model): # Blog 라는 이름의 객체를 만들겠다.
    title = models.CharField(max_length=200) # title 이름으로 최대 200 글자의 데이터를 받겠다.
    pub_date = models.DateTimeField('date published') # pub_date 라는 이름으로 시간 날짜 데이터를 받겠다.
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)


    # M : N을 위한 속성
    likes = models.ManyToManyField(
        User, #User 모델과 Blog 모델을 M : N 관계로 두겠다.
        through= 'Like', # Like라는 중개 모델을 통해 M : N  관계를 맺는다.
        through_fields=('blog','user'), # Like에 blog 속성, user 속성을 추가하겠다.

        related_name= 'likes' #  1: N 관계에서 blog와 연결된 comment를 가져올 때 
                                # comment_set으로 가져왔는데, related_name을 설정하면 blog.like_set이 아니라
                                # blog.likes로 blog와 연결된 like를 가져올 수 있다.
    )

    #이 객체를 가르키는 말을 title로 정하겠다.
    def __str__(self):
        return self.title
    # 몇 개의 like와 연결되어 있는가를 보여준다.    
    def like_count(self):
        return self.likes.count()

class Like(models.Model):
    #Blog의 through_fields와 순서가 같아야 한다.
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, null= True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, null = True)

class Comment(models.Model):
    body = models.TextField()
    #Blog 모델과 관계를 맺어준다. 1: N에서 N의 속성으로 들어간다.
    #on_delete는 관계를 맺고 있는 Blog 객체가 삭제되면 관련된 Comment도 삭제시킨다.

    blog = models.ForeignKey(Blog, on_delete= models.CASCADE, null= True)

    def __str__(self):
        return self.body
