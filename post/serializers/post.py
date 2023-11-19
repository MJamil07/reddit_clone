from rest_framework import serializers
from post.models import Post
from subreddits.models import Subreddit
from post.models import UpVote , DownVote
from comments.models import Comment
from comments.serializers import ListCommentSerializer

class ListPostSerializer(serializers.ModelSerializer):
      
      upvote = serializers.SerializerMethodField()
      downvote = serializers.SerializerMethodField()
      comment = serializers.SerializerMethodField()
      
      class Meta:
            model = Post
            fields = '__all__'
            
      def get_upvote(self , post):                         
            return UpVote.objects.filter(post = post.id).count()
            
      def get_downvote(self , post):
            return DownVote.objects.filter(post = post.id).count()
      
      def get_comment(self , post):
            return ListCommentSerializer( Comment.objects.filter(post=post.id).order_by('-create_at') , many = True).data

class PostSerializer(serializers.ModelSerializer):
      
      class Meta:

            model = Post
            fields = ('title' ,  'interest'  )
            
      def validate(self , new_post):
            
            subreddit_id = new_post.get('subreddit' , None)
            
            # * `subreddit_id` is None post upload for user indivitualy
            if subreddit_id is None: return new_post
            else:
                  # * `subreddit_id` is exist the post upload for subreddit community
                 subreddit = Subreddit.objects.get(id = subreddit_id)
                 
                 # * check if community exists are not
                 if subreddit is None:
                       return serializers.ValidationError("Given Subreddit is not exist")
                 
            return new_post