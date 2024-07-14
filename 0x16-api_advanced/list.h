#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * struct ListNode - singly linked list
 * @data: void pointer to store any data type
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct ListNode
{
    void *data;
    struct ListNode *next;
} ListNode;

/**
 * struct SubredditInfo - stores subreddit information
 * @name: name of the subreddit
 * @num_subscribers: number of subscribers
 * @top_posts: list of top 10 post titles
 */
typedef struct SubredditInfo
{
    char *name;
    int num_subscribers;
    ListNode *top_posts;
} SubredditInfo;

ListNode *add_nodeint(ListNode **head, void *data);
void free_listint(ListNode *head);
SubredditInfo *create_subreddit_info(char *name);
void add_top_post(SubredditInfo *subreddit, char *title);
int get_num_subscribers(SubredditInfo *subreddit);

#endif /* LISTS_H */
