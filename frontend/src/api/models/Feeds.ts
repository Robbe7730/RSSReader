/* tslint:disable */
/* eslint-disable */
/**
 * PostgREST API
 * This is a dynamic API generated by PostgREST
 *
 * The version of the OpenAPI document: 7.0.1 (UNKNOWN)
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface Feeds
 */
export interface Feeds {
    /**
     * Note:
     * This is a Primary Key.<pk/>
     * @type {number}
     * @memberof Feeds
     */
    id: number;
    /**
     * 
     * @type {string}
     * @memberof Feeds
     */
    name: string;
    /**
     * 
     * @type {string}
     * @memberof Feeds
     */
    url: string;
    /**
     * 
     * @type {number}
     * @memberof Feeds
     */
    priority: number;
    /**
     * 
     * @type {boolean}
     * @memberof Feeds
     */
    hidden: boolean;
    /**
     * 
     * @type {string}
     * @memberof Feeds
     */
    createdAt: string;
    /**
     * 
     * @type {string}
     * @memberof Feeds
     */
    updatedAt: string;
}

export function FeedsFromJSON(json: any): Feeds {
    return FeedsFromJSONTyped(json, false);
}

export function FeedsFromJSONTyped(json: any, ignoreDiscriminator: boolean): Feeds {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
        'name': json['name'],
        'url': json['url'],
        'priority': json['priority'],
        'hidden': json['hidden'],
        'createdAt': json['created_at'],
        'updatedAt': json['updated_at'],
    };
}

export function FeedsToJSON(value?: Feeds | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'name': value.name,
        'url': value.url,
        'priority': value.priority,
        'hidden': value.hidden,
        'created_at': value.createdAt,
        'updated_at': value.updatedAt,
    };
}


